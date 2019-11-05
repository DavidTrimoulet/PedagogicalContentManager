'use strict';
angular.module('myApp.bloom', ['ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/bloom', {
            templateUrl: '/static/bloom/bloom.html',
            controller: 'BloomCtrl'
        });
    }])

    .controller('BloomCtrl', function ($scope, $http) {
        $http({
            method: 'GET',
            url: 'http://localhost:8000/api/v1/bloom_taxonomies/'
        }).then(function successCallback(response) {
            $scope.bloom_taxonomies = response.data;
            var clean_taxonomies = {};
            $scope.bloom_taxonomies.forEach(function (item, index) {
                if (!(item.family in clean_taxonomies)) {
                    clean_taxonomies[item.family] = []
                }
                clean_taxonomies[item.family].push(item.verb);
            });
            $scope.taxonomies_head = Object.keys(clean_taxonomies);
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
            console.log($scope.taxonomies_data[0].length);
            var i, j;
            for (i = 0; i < $scope.taxonomies_head.length; i++) {
                for (j = 0; j < longest_list_length; j++) {
                    console.log(i, j);
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
    });