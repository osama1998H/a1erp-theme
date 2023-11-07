/*
* Side Menu
*/

import Menu from './components/Menu.vue';

new Vue({
    el: $('#side-menu-component')[0],
    render: h => h(Menu)
});

String.prototype.beginsWith = function (string) {
    return (this.indexOf(string) === 0);
};
