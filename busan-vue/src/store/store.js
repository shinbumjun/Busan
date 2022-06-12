import router from '@/router'
import vue from 'vue'
import vuex from 'vuex'

Vue.use(Vuex)

export const store = new Vuex.Store({
    state: {
      todoItems: []
    }
  });

const userStore = {
    state: {
        user_id: '',
        name: '',
        email:'',
        token: ''
    },
    mutations: {
        login: function (state, payload) {
            state.user_id = payload.user_id
            state.name = payload.name
            state.emial = payload.email
            state.token = payload.token
        },
        loginCheck: function (state) {
            if (!state.token) {
                router.push({
                    name: 'login'
                }).catch(error => {
                    console.log(error)
                })
            }
        }

    }
}

export default userStore