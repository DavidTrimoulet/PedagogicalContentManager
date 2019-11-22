'use strict';

// Declare app level module which depends on views, and core components
angular.module('myApp', [
  'ngRoute',
  'myApp.home',
  'myApp.bloom',
  'myApp.skill',
  'myApp.version',
  'myApp.navBar',
  'myApp.rubricks',
  'myApp.problem',
  'autocomplete.bloom',
  'autocomplete.skill'
]).config(['$locationProvider', '$routeProvider', function($locationProvider, $routeProvider) {
  $locationProvider.hashPrefix('!');
  $routeProvider.otherwise({redirectTo: '/home'});
}]);

angular.module('sideComponent', [

]);