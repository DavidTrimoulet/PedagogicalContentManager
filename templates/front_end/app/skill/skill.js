'use strict';

angular.module('myApp.skill', ['ngRoute', 'ngMaterial'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/skill', {
            templateUrl: '/static/skill/skill.html',
            controller: 'SkillCtrl'
        });
    }])

    .controller('SkillCtrl', function ($scope, $http) {
        $scope.update = function () {
            $http({
                method: 'GET',
                url: 'http://localhost:8000/api/v1/skill/'
            }).then(function successCallback(response) {
                $scope.skills = response.data;
            }, function errorCallback(response) {
                // called asynchronously if an error occurs
                // or server returns response with an error status.
            });
            $http({
                method: 'GET',
                url: 'http://localhost:8000/api/v1/bloom_taxonomies/'
            }).then(function successCallback(response) {
                $scope.taxonomies = response.data;
            }, function errorCallback(response) {
                // called asynchronously if an error occurs
                // or server returns response with an error status.
            });
        };
        $scope.update();
        $scope.skill = {
            taxonomy: {},
            text: ""
        };


    });

angular.module('autocomplete', ['ngMaterial'])
    .controller('autocompleteCtrl', AutocompleteCtrl);

function AutocompleteCtrl($timeout, $q, $log, $scope, $http) {
    var self = this;

    self.simulateQuery = false;
    self.isDisabled = false;

    // list of `state` value/display objects
    $http({
        method: 'GET',
        url: 'http://localhost:8000/api/v1/bloom_taxonomies/'
    }).then(function successCallback(response) {
        self.taxonomies = response.data;
    }, function errorCallback(response) {
        // called asynchronously if an error occurs
        // or server returns response with an error status.
    });
    self.querySearch = querySearch;
    self.selectedItemChange = selectedItemChange;
    self.searchTextChange = searchTextChange;

    self.addTaxonomy = function (skill) {
            var skillToPut = {"verb":$scope.selectedItem.verb, "text":skill.text};
            console.log("adding taxonomy:" , $scope.selectedItem, "and text : ", skill.text);
            $http({
                method: 'PUT',
                url: 'http://localhost:8000/api/v1/skill/',
                data: skillToPut
            }).then(function successCallback(response) {
                $scope.skills = response.data;
            }, function errorCallback(response) {
                // called asynchronously if an error occurs
                // or server returns response with an error status.
            });
        };

    function querySearch(query) {
        var results =  findVerb(query);
        return results;
    }

    function searchTextChange(text) {
        $log.info('Text changed to ' + text);
    }

    function selectedItemChange(item) {
        $scope.selectedItem = item;
        $log.info('Item changed to ' + JSON.stringify(item));
    }

    function findVerb(query) {
        return Object.values(Object.fromEntries(Object.entries(self.taxonomies).filter(([k, v]) => v.verb.includes(query))));;
    }
}

