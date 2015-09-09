//// Copyright (c) Microsoft Corporation. All rights reserved

(function () {
    var module = angular.module("AngularWinJSApp", ["winjs"]);
    module.controller("AngularWinJSAppController", function ($scope, $http, $interval) {
        $scope.mode = "SENSOR";
        
        $http.get("/api/getData")
            .success(function(data) 
                {$scope.week = data;});
                        
        $scope.sync = function () {
            $http.post("/api/postData", $scope.week);
        };
        
        $scope.test = function () {
            alert("Hello : "+$scope.mode);
        };
        
         $interval(callAtInterval, 1000);
        function callAtInterval() {
            $http.get("/api/getState")
                .success(function(data) 
                    {$scope.state = data.state;});
        }

        //$http.get("/api/weekdata")
        //    .success(function(data) {$scope.items2 = data;});

    });  
})();
