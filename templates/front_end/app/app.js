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
    'autocomplete.skill',
    'autocomplete.problem'
]).config(['$locationProvider', '$routeProvider', '$httpProvider', function ($locationProvider, $routeProvider,$httpProvider) {
    $locationProvider.hashPrefix('!');
    $routeProvider.otherwise({redirectTo: '/home'});
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

angular.module('sideComponent', []);