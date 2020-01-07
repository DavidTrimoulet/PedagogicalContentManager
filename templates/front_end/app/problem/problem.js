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
        $scope.title = "";
        $scope.text = "";
        $scope.tinymceOptions = {
            plugins: 'link image code',
            toolbar: 'undo redo | bold italic | alignleft aligncenter alignright | code',

        };
        $scope.update = function ($http, $scope) {

        };
        $scope.getProblemContent = function (title) {
            $log.info("getting data for " + title);
            $http({
                method: 'POST',
                url: 'http://127.0.0.1:8000/api/v1/problems/',
                data: {'problem': title}
            }).then(function successCallback(response) {
                $log.info("getting problem content");
                $scope.problemContent = response.data;
            }, function errorCallback(response) {
                // called asynchronously if an error occurs
                // or server returns response with a'autocomplete.skill'n error status.
            });
        };
        $scope.updateProblemContent = function () {
            $log.info("updating content");
            $http({
                method: 'PUT',
                url: 'http://127.0.0.1:8000/api/v1/problems/',
                data: {'title': $scope.title }
            }).then(function successCallback(response) {
                $log.info("getting problem content");
                $scope.problemContent = response.data;
            }, function errorCallback(response) {
                // called asynchronously if an error occurs
                // or server returns response with a'autocomplete.skill'n error status.
            });
        };
        $scope.updateProblemTitle = function () {
            $log.info("updating Title");
            $http({
                method: 'PUT',
                url: 'http://127.0.0.1:8000/api/v1/problems/',
                data: {'text': $scope.text }
            }).then(function successCallback(response) {
                $log.info("getting problem content");
                $scope.problemContent = response.data;
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

    self.problems = [];
    self.problemContent = [];
    self.querySearch = querySearch;
    self.selectedItemChange = selectedItemChange;
    self.update = update;


    $http({
        method: 'GET',
        url: 'http://127.0.0.1:8000/api/v1/problems/'
    }).then(function successCallback(response) {
        self.problems = response.data;
    }, function errorCallback(response) {
        // called asynchronously if an error occurs
        // or server returns response with a'autocomplete.skill'n error status.
    });


    function querySearch(query) {
        return findTitle(query);
    }

    function selectedItemChange(item) {
        self.selectedItem = item;
        $scope.getProblemContent(item.title);
    }

    function findTitle(query) {
        $log.info("problems:", self.problems);
        return self.problems.filter(function (item) {
            return item.title.includes(query);
        });
    }

    function update() {


    }
}