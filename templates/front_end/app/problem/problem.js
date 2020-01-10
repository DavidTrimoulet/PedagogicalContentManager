'use strict';

angular.module('myApp.problem', ['ngRoute', 'ui.tinymce'])

    .config(['$routeProvider', '$httpProvider', function ($routeProvider, $httpProvider) {
        $routeProvider.when('/problem', {
            templateUrl: '/static/app/problem/problem.html',
            controller: 'ProblemCtrl'
        });
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }])

    .controller('ProblemCtrl', function ($scope, $http, $log) {
        $scope.selectedProblem = {};
        $scope.tinymceOptions = {
            plugins: 'link image code autoresize',
            toolbar: 'undo redo | bold italic | alignleft aligncenter alignright | code',
            images_upload_handler: function (blobInfo, success, failure) {
                $log.info("blob", blobInfo.blob());
                //var dataToSend = { 'filename':blobInfo.blob().name };
                var formData = new FormData();
                formData.append('image', blobInfo.blob(), blobInfo.blob().name);
                $log.info(formData);
                $http({
                    method: 'POST',
                    url: 'http://127.0.0.1:8000/api/v1/uploadImage/',
                    transformRequest: angular.identity,
                    headers: {
                        'Content-Type': undefined
                    },
                    data: formData
                }).then(function successCallback(response) {
                    success(response.data['url']);
                }, function errorCallback(response) {
                    failure();
                    // called asynchronously if an error occurs
                    // or server returns response with a'autocomplete.skill'n error status.
                });
            }

        };
        $scope.update = function ($http, $scope) {

        };
        $scope.getProblemContent = function (problem) {
            $log.info("getting data for " + problem.title);
            $http({
                method: 'POST',
                url: 'http://127.0.0.1:8000/api/v1/problems/',
                data: {'problem': problem.title}
            }).then(function successCallback(response) {
                $log.info("getting problem content");
                $log.info(response.data);
                $scope.selectedProblem = problem;
                $scope.problemContent = response.data;
            }, function errorCallback(response) {
                // called asynchronously if an error occurs
                // or server returns response with a'autocomplete.skill'n error status.
            });
        };

        $scope.updateProblemContent = function () {
            $http({
                method: 'PUT',
                url: 'http://127.0.0.1:8000/api/v1/problems/',
                data: $scope.problemContent
            }).then(function successCallback(response) {

            }, function errorCallback(response) {
                // called asynchronously if an error occurs
                // or server returns response with a'autocomplete.skill'n error status.
            });
        };

        $scope.updateProblemTitle = function () {
            $http({
                method: 'PUT',
                url: 'http://127.0.0.1:8000/api/v1/problems/',
                data: $scope.selectedProblem
            }).then(function successCallback(response) {

            }, function errorCallback(response) {
                // called asynchronously if an error occurs
                // or server returns response with a'autocomplete.skill'n error status.
            });
        };
        $log.info("tinymce controller loaded");
    });

angular.module('autocomplete.problem', ['ngMaterial'])
    .controller('ProblemAutocompleteCtrl', ProblemAutocompleteCtrl);

function ProblemAutocompleteCtrl($timeout, $q, $log, $scope, $http) {
    var self = this;
    self.simulateQuery = false;
    self.isDisabled = false;
    self.noCache = true;
    self.problems = [];
    self.querySearch = querySearch;
    self.selectedItemChange = selectedItemChange;
    self.update = function () {
        $http({
            method: 'GET',
            url: 'http://127.0.0.1:8000/api/v1/problems/'
        }).then(function successCallback(response) {
            self.problems = response.data;
        }, function errorCallback(response) {
            // called asynchronously if an error occurs
            // or server returns response with a'autocomplete.skill'n error status.
        });
    }
    self.update();

    function querySearch(query) {
        self.update();
        return findTitle(query);
    }

    function selectedItemChange(item) {
        if (!angular.isUndefined(item)) {
            self.selectedItem = item;
            $scope.selectedProblem = item;
            $scope.getProblemContent(item);
        }
    }

    function findTitle(query) {
        return self.problems.filter(function (item) {
            return item.title.includes(query);
        });
    }

    function update() {

    }
}