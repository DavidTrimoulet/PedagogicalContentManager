'use strict';

angular.module('myApp.problem', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/problem', {
    templateUrl: '/static/problem/problem.html',
    controller: 'ProblemCtrl'
  });
}])

.controller('ProblemCtrl', [function($scope, $http) {
    $scope.title = getTitle; //models.CharField(max_length=256)
    $scope.text = getText; //models.CharField(max_length=1024)
    $scope.keyword = getKeywords; //models.ManyToManyField(KeyWord)
    $scope.skill = getSkill; //models.ManyToManyField(Skill)
    $scope.hint_and_advise = getHint;//models.OneToOneField(HintAndAdvise, on_delete='cascade', null=True)
    $scope.action_plan = getActionPlan; //models.ManyToManyField(ActionPlan)
    $scope.validation_questions = getValidationQuestion; //models.ManyToManyField(ValidationQuestion)
    $scope.resources = getRessources; //models.ManyToManyField(Resource)
    $scope.solution = getSolution; //models.ManyToManyField(Solution)
    $scope.versions = getVersions; //models.ManyToManyField(Version)
    function getHttpData(url) {
      $http({
                method: 'GET',
                url: 'http://127.0.0.1:8000/api/v1/problem/'
            }).then(function successCallback(response) {
                var rubricks = response.data;
                $scope.rubricks = rubricks.map(getItemKeyValue);
                console.log("scope.rubricks :", $scope.rubricks);
            }, function errorCallback(response) {
                // called asynchronously if an error occurs
                // or server returns response with an error status.
            });
    }
    function getTitle() {
      return getHttpData("");
    }
}]);