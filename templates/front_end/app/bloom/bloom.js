'use strict';
angular.module('myApp.bloom', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/bloom', {
    templateUrl: '/static/bloom/bloom.html',
    controller: 'BloomCtrl'
  });
}])

.controller('BloomCtrl', function($scope, $http) {
  $http({
    method: 'GET',
    url: 'http://localhost:8000/api/v1/bloom_taxonomies/'
  }).then(function successCallback(response) {
    var bloom_taxonomies = response.data;
    var clean_taxonomies = {};
    bloom_taxonomies.forEach(function (item, index) {
      if( !(item.family in clean_taxonomies ) ){
        clean_taxonomies[item.family] = []
      }
      clean_taxonomies[item.family].push(item.verb)
    });
  }, function errorCallback(response) {
    // called asynchronously if an error occurs
    // or server returns response with an error status.
  });
});