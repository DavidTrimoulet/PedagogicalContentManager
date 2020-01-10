'use strict';

angular.module('myApp.rubricks', ['ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/rubricks', {
            templateUrl: '/static/app/rubricks/rubricks.html',
            controller: 'RubricksCtrl'
        });
    }])

    .controller('RubricksCtrl', function ($scope, $http, $log) {
        $scope.rubricks = [];

        $scope.getData = function () {
            $http({
                method: 'GET',
                url: 'http://127.0.0.1:8000/api/v1/skill_rubricks/'
            }).then(function successCallback(response) {
                var rubricks = response.data;
                $scope.rubricks = rubricks.map(getItemKeyValue);
            }, function errorCallback(response) {
                // called asynchronously if an error occurs
                // or server returns response with an error status.
            });
        };

        function getItemKeyValue (item) {
            return {'key': item.skill.taxonomy.verb + " " + item.skill.text, 'value': item};
        };

        function findItem(query) {
            var skills = Object.values(Object.fromEntries(Object.entries($scope.rubricks).filter(([k, v]) => k.includes(query))));
            return skills;
        }

        $scope.getData();
    });

angular.module('autocomplete.skill', ['ngMaterial'])
    .controller('SkillAutocompleteCtrl', SkillAutocompleteCtrl);

function SkillAutocompleteCtrl($timeout, $q, $log, $scope, $http) {
    var self = this;
    self.rubricks = {'Level_a': '', 'Level_b': '', 'Level_c': '', 'Level_d': '',};
    self.simulateQuery = false;
    self.isDisabled = false;
    self.added = "";
    self.style = {'visibility': 'invisible'};

    // list of `state` value/display objects
    $http({
        method: 'GET',
        url: 'http://localhost:8000/api/v1/skill/'
    }).then(function successCallback(response) {
        self.skill = response.data;
    }, function errorCallback(response) {
        // called asynchronously if an error occurs
        // or server returns response with an error status.
    });
    self.querySearch = querySearch;
    self.selectedItemChange = selectedItemChange;
    self.getItemKeyValue = getItemKeyValue;
    self.update = update;

    function querySearch(query) {
        return findVerb(query);
    }

    function selectedItemChange(item) {
        if (!(item === undefined)) {
            var found = $scope.rubricks.find(e => e.key == item.key);
            if (!(found === undefined)) {
                self.selectedItem = found;
            } else {
                self.selectedItem = {
                    'key': item.key,
                    'value': {
                        'skill': {'taxonomy': item.value.taxonomy, 'text': item.value.text},
                        'level_a': '',
                        'level_b': '',
                        'level_c': '',
                        'level_d': ''
                    }
                };
                $scope.rubricks.push(self.selectedItem);
            }
        }
    }

    function getItemKeyValue(item) {
        return {'key': item.taxonomy.verb + " " + item.text, 'value': item};
    }

    function findVerb(query) {
        var elements = Object.values(Object.fromEntries(Object.entries(self.skill).filter(([k, v]) => v.taxonomy.verb.includes(query) || v.text.includes(query))));
        return elements.map(getItemKeyValue);
    }

    function update() {
        if (!(self.selectedItem === undefined)) {
            //$log.info("mise à jour des rubricks :", $scope.rubricks);
            $scope.rubricks = $scope.rubricks.filter(function (item) {
                if(item.key != undefined){
                    return item;
                }
            });
            //$log.info("rubricks cleaned :", $scope.rubricks);
            $scope.rubricks.forEach(function (item) {
                var rubricksToPut = {
                    "verb": item.value.skill.taxonomy.verb,
                    "text": item.value.skill.text,
                    "level_a": item.value.level_A,
                    "level_b": item.value.level_B,
                    "level_c": item.value.level_C,
                    "level_d": item.value.level_D
                };
                //$log.info(rubricksToPut);
                $http({
                    method: 'PUT',
                    url: 'http://localhost:8000/api/v1/skill_rubricks/',
                    data: rubricksToPut
                }).then(function successCallback(response) {
                    self.added = response.status;
                }, function errorCallback(response) {
                    // called asynchronously if an error occurs
                    // or server returns response with an error status.
                });
            });
        }

    }
}