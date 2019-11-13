'use strict';
angular.module('myApp.bloom', ['ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/bloom', {
            templateUrl: '/static/bloom/bloom.html',
            controller: 'BloomCtrl'
        });
    }])

    .controller('BloomCtrl', function ($scope, $http) {
        $scope.form = {};
        $scope.taxonomy = [];
        $scope.getData = function () {
            console.log("Getting Data");
            $http({
                method: 'GET',
                url: 'http://localhost:8000/api/v1/bloom_taxonomies/'
            }).then(function successCallback(response) {
                $scope.bloom_taxonomies = response.data;
                var clean_taxonomies = {};
                $scope.taxonomies_level = {}
                $scope.bloom_taxonomies.forEach(function (item, index) {
                    if (!(item.family in clean_taxonomies)) {
                        clean_taxonomies[item.family] = [];
                        $scope.taxonomies_level[item.family] = item.level;
                    }
                    clean_taxonomies[item.family].push(item.verb);
                });
                $scope.taxonomies_head = Object.keys($scope.taxonomies_level);
                var longest_list_length = 0;
                $scope.taxonomies_head.forEach(function (item, index) {
                    if (clean_taxonomies[item].length > longest_list_length) {
                        longest_list_length = clean_taxonomies[item].length;
                    }
                });
                $scope.taxonomies_data = new Array(longest_list_length);
                var k;
                for (k = 0; k < $scope.taxonomies_data.length; k++) {
                    $scope.taxonomies_data[k] = new Array($scope.taxonomies_head.length);
                }
                var i, j;
                for (i = 0; i < $scope.taxonomies_head.length; i++) {
                    for (j = 0; j < longest_list_length; j++) {
                        if (j >= clean_taxonomies[$scope.taxonomies_head[i]].length) {
                            $scope.taxonomies_data[j][i] = "";
                        } else {
                            $scope.taxonomies_data[j][i] = clean_taxonomies[$scope.taxonomies_head[i]][j];
                        }
                    }
                }
            }, function errorCallback(response) {
                // called asynchronously if an error occurs
                // or server returns response with an error status.
            });
        };
        $scope.update = function (taxonomy, index) {

            var taxonomyToPut = {
                "level": $scope.taxonomies_level[$scope.taxonomies_head[index]],
                "verb": taxonomy,
                "family": $scope.taxonomies_head[index]
            };
            console.log("adding taxonomy:", taxonomyToPut);
            $http({
                method: 'PUT',
                url: 'http://localhost:8000/api/v1/bloom_taxonomies/',
                data: taxonomyToPut
            }).then(function successCallback(response) {
                $scope.taxonomy = [];
                $scope.form.addTaxonomyForm.$setPristine();
                console.log($scope);
                $scope.getData();
            }, function errorCallback(response) {
                // called asynchronously if an error occurs
                // or server returns response with an error status.
            });
        };
        $scope.getData();
    });