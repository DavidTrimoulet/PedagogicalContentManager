'use strict';

angular.module('myApp.home', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/home', {
    templateUrl: '/static/home/home.html',
    controller: 'homeCtrl'
  });
}])

.controller('View2Ctrl', [function() {

}]);