import router from '@/router'


const userStore = {
    state: {
        user_id: '',
        name: '',
        token: ''
    },
    mutations: {
        login: function (state, payload) {
            state.user_id = payload.user_id
            state.name = payload.name
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