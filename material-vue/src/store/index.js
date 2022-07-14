import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({

    namespace: true,
    state: {
        drawer: true,
        access: '',
        refresh: ''
    },
    mutations: {
        initializeStore(state) {
            if (localStorage.getItem('access')) {
                state.access = localStorage.getItem('access')
                state.refresh = localStorage.getItem('refresh')
            } else {
                state.access = ''
                state.refresh = ''
            }
        }
        ,
        setAccess(state, access) {
            state.access = access
        },
        setRefresh(state, refresh) {
            state.refresh = refresh
        },

        toggleDrawer(state) {
            state.drawer = !state.drawer;
        }
    },
    actions: {
        TOGGLE_DRAWER({commit}) {
            commit('toggleDrawer');
        },

    },
    getters:
        {
            DRAWER_STATE(state) {
                return state.drawer;
            }
        }
})
;
