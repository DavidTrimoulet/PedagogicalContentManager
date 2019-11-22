angular.module('myApp.navBar', ['ngRoute'])
    .component('navBar', {
        templateUrl: '/static/navbar/navbar.html',
        controller: function NavbarController() {
            this.pages = [
                {
                    name: 'bloom',
                    folder: 'bloom'
                },
                {
                    name: 'skill',
                    folder: 'skill'
                },
                {
                    name: 'rubricks',
                    folder: 'rubricks'
                },
                {
                    name: 'problem',
                    folder: 'problem'
                }
            ];
        }
    });