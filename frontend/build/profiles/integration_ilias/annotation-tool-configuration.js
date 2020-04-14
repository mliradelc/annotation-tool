/**
 *  Copyright 2012, Entwine GmbH, Switzerland
 *  Licensed under the Educational Community License, Version 2.0
 *  (the "License"); you may not use this file except in compliance
 *  with the License. You may obtain a copy of the License at
 *
 *  http://www.osedu.org/licenses/ECL-2.0
 *
 *  Unless required by applicable law or agreed to in writing,
 *  software distributed under the License is distributed on an "AS IS"
 *  BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
 *  or implied. See the License for the specific language governing
 *  permissions and limitations under the License.
 *
 */

/**
 * Module containing the tool configuration
 * @module annotation-tool-configuration
 */
define(["jquery",
        "underscore",
        "backbone",
        "util",
        "models/user",
        "roles",
        "player_adapter_HTML5",
        "localstorage",
        "cryptojs.md5"
        // Add the files (PlayerAdapter, ...) required for your configuration here
        ],

    function ($, _, Backbone, util, User, ROLES, HTML5PlayerAdapter) {

        "use strict";

        var backboneSync = Backbone.sync;

        /**
         * Synchronize models with an annotation tool backend
         */
        Backbone.sync = function (method, model, options) {

            // The backend expects `application/x-www-form-urlencoded data
            // with anything nested deeper than one level transformed to a JSON string
            options.processData = true;

            options.data = options.attrs || model.toJSON(options);

            // Some models (marked with `mPOST`) need to always be `PUT`, i.e. never be `POST`ed
            if (model.noPOST && method === "create") {
                method = "update";
            }

            options.beforeSend = function () {
                this.url = "../../extended-annotations" + this.url;
            };

            return backboneSync.call(this, method, model, options);
        };

        // Initiate loading the video metadata from Opencast
        var mediaPackageId = util.queryParameters.id;
        var mediaURL = util.queryParameters.mediaURL;

        //Only for when mediaURL is signed
        var urlHash = util.queryParameters.UzKhash;
        var urlEndTime = util.queryParameters.UzKendtime;

        if (urlHash){
                mediaURL = mediaURL.concat('?UzKendtime=', urlEndTime, '&UzKhash=', urlHash, '=');
        }

        //Load user metadata from ilias
        var ref_id = util.queryParameters.refid;
        var auth_hash = util.queryParameters.auth;
        $.support.cors = true;

        // Get user data from Opencast
        var user = $.ajax({
            url: "/info/me.json",
            dataType: "json"
        });
       
        /**
         * Annotations tool configuration object
         * @alias module:annotation-tool-configuration.Configuration
         */
        var Configuration = {
            /**
             * The minmal duration used for annotation representation on timeline
             * @alias module:annotation-tool-configuration.Configuration.MINIMAL_DURATION
             * @memberOf module:annotation-tool-configuration.Configuration
             * @type {Object}
             */
            MINIMAL_DURATION: 1,

            /**
             * Define the number of categories per tab in the annotate box.
             * The bigger this number, the thinner the columns for the categories.
             * @alias module:annotation-tool-configuration.Configuration.CATEGORIES_PER_TAB
             * @memberOf module:annotation-tool-configuration.Configuration
             * @type {Number}
             */
            CATEGORIES_PER_TAB: 7,

            /**
             * Define if the localStorage should be used or not
             * @alias module:annotation-tool-configuration.Configuration.localStorage
             * @type {boolean}
             * @readOnly
             */
            localStorage: false,

            /**
             * Offer the user a spreadsheet version of the annotations for download.
             * @alias module:annotation-tool-configuration.Configuration.export
             * @param {Video} video The video to export
             * @param {Track[]} tracks The tracks to include in the export
             * @param {Category[]} categories The tracks to include in the export
             * @param {Boolean} freeText Should free-text annotations be exported?
             */
            export: function (video, tracks, categories, freeText) {
                var parameters = new URLSearchParams();
                _.each(tracks, function (track) {
                    parameters.append("track", track.id);
                });
                _.each(categories, function (category) {
                    parameters.append("category", category.id);
                });
                parameters.append("freetext", freeText);
                window.location.href =
                    "../extended-annotations/videos/" +
                    video.id +
                    "/export.csv?" +
                    parameters;
            },

            /**
             * Define if the structured annotations are or not enabled
             * @alias module:annotation-tool-configuration.Configuration.isStructuredAnnotationEnabled
             * @return {boolean} True if this feature is enabled
             */
            isStructuredAnnotationEnabled: function () {
                return true;
            },

            /**
             * Define if the free text annotations are or not enabled
             * @alias module:annotation-tool-configuration.Configuration.isFreeTextEnabled
             * @return {boolean} True if this feature is enabled
             */
            isFreeTextEnabled: function () {
                return true;
            },

            /**
             * Get the current video id (video_extid)
             * @alias module:annotation-tool-configuration.Configuration.getVideoExtId
             * @return {Promise.<string>} video external id
             */
            getVideoExtId: function () {
                return $.when(mediaPackageId);
            },

            /**
             * Returns the time interval between each timeupdate event to take into account.
             * It can improve a bit the performance if the amount of annotations is important.
             * @alias module:annotation-tool-configuration.Configuration.getTimeupdateIntervalForTimeline
             * @return {number} The interval
             */
            getTimeupdateIntervalForTimeline: function () {
                // TODO Check if this function should be linear
                return Math.max(500, this.getAnnotations().length * 3);

            },

            /**
             * Get the external parameters related to video. The supported parameters are now the following:
             *     - title: The title of the video
             *     - src_owner: The owner of the video in the system
             *     - src_creation_date: The date of the course, when the video itself was created.
             * @alias module:annotation-tool-configuration.Configuration.getVideoParameters
             * @example
             * {
             *     video_extid: 123, // Same as the value returned by getVideoExtId
             *     title: "Math lesson 4", // The title of the video
             *     src_owner: "Professor X", // The owner of the video in the system
             *     src_creation_date: "12-12-1023" // The date of the course, when the video itself was created.
             * }
             * @return {Object} The literal object containing all the parameters described in the example.
             */
            getVideoParameters: function () {
                return {
                    title: "Annotation Tool",
                    src_owner: "",
                    src_creaton_date: ""
                }
            },

            /**
             * Checks if the auth hash includes the admin key
             * @alias module:annotation-tool-configuration.Configuration.getUserRoleFromHash
             * @param {string[]} username The user logged in
             * @param {string[]} courseRef The course reference from ilias
             * @param {string[]} authHash The authorization hash to verify the user
             * @return {Promise.<ROLE>} The corresponding user role in the annotations tool
             */
            getUserRoleFromHash: function (username, courseRef, authHash) {
                // Preparing variables
                var initialConcat = '';
                var adminHash = '';
                var userHash = ''; 
                initialConcat = initialConcat.concat(username.toUpperCase(), courseRef);

                // Calculate hash
                adminHash = CryptoJS.MD5(adminHash.concat(initialConcat, '1')).toString();
                userHash = CryptoJS.MD5(userHash.concat(initialConcat, '0')).toString();
                if (authHash == adminHash){
                    return ROLES.ADMINISTRATOR;
                } else if (authHash == userHash){
                   return ROLES.USER;
                } else {
                    return 'undefined';
                }
            },

            /**
             * Authenticate the user
             * @alias module:annotation-tool-configuration.Configuration.authenticate
             */
            authenticate: function () {
                user.then(function (userData) {
                    return $.when(userData.user, this.getUserRoleFromHash(userData.user.username,ref_id,auth_hash));
                }.bind(this)).then(function (user, role) {
                    if (role == 'undefined') {
                        this.trigger(this.EVENTS.USER_NOT_AUTHORIZED);
                    } 
                    this.user = new User({
                        user_extid: user.username,
                        nickname: user.username,
                        email: user.email,
                        role: role
                    });
                    return this.user.save();
                }.bind(this)).then(function () {
                    this.trigger(this.EVENTS.USER_LOGGED);
                }.bind(this));
            },

            /**
             * Log out the current user
             * @alias module:annotation-tool-configuration.Configuration.logout
             */
            logout: function () {
                window.location = "/j_spring_security_logout";
            },

            /**
             * Function to load the video
             * @alias module:annotation-tool-configuration.Configuration.loadVideo
             * @param {HTMLElement} container The container to create the video player in
             */
            loadVideo: function (container) {
                 var videoElement = document.createElement("video");
                container.appendChild(videoElement);
                var videoURL = {
                    src: mediaURL,
                    type: "application/x-mpegURL"
                }
                this.playerAdapter = new HTML5PlayerAdapter(
                    videoElement, videoURL
                );
                this.trigger(this.EVENTS.VIDEO_LOADED);
                
            }
        };

        return Configuration;
    }
);
