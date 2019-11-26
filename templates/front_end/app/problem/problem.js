'use strict';

angular.module('myApp.problem', ['ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/problem', {
            templateUrl: '/static/problem/problem.html',
            controller: 'ProblemCtrl'
        });
    }])

    .controller('ProblemCtrl', function ($scope, $http) {

        $scope.updateData = getData;
        function getData(ProblemTitle) {
            if (ProblemTitle != "") {
                $http({
                    method: 'POST',
                    url: 'http://127.0.0.1:8000/api/v1/problems/',
                    data: {'title': ProblemTitle}
                }).then(function successCallback(response) {
                    $scope.problem = response.data;
                }, function errorCallback(response) {
                    // called asynchronously if an error occurs
                    // or server returns response with an error status.
                });
            }

        }

    });

angular.module('autocomplete.problem', ['ngMaterial'])
    .controller('ProblemAutocompleteCtrl', ProblemAutocompleteCtrl);

function ProblemAutocompleteCtrl($timeout, $q, $log, $scope, $http) {
    var self = this;
    self.simulateQuery = false;
    self.isDisabled = false;

    self.titles = [];

    self.querySearch = querySearch;
    self.selectedItemChange = selectedItemChange;
    self.update = update;

    function getProblemsTitle() {
        $http({
                    method: 'GET',
                    url: 'http://127.0.0.1:8000/api/v1/problems/'
                }).then(function successCallback(response) {
                    var problems = response.data;
                    self.titles =  problems.map(getItemTitle);
                }, function errorCallback(response) {
                    // called asynchronously if an error occurs
                    // or server returns response with a'autocomplete.skill'n error status.
                });
    }

    getProblemsTitle();
    function getItemTitle(item) {
        $log.info("item:", item);
        return item.title;
    }

    function querySearch(query) {
        return findTitle(query);
    }

    function selectedItemChange(item) {
        self.selectedItem = item;
        $scope.updateData(item);
    }

    function findTitle(query) {
        $log.info("titles:", self.titles);
        return self.titles.filter(function (item) {
         return item.includes(query);
        });
    }

    function update() {


    }
}