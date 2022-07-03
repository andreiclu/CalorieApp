<template>
  <router-view />
</template>


<script>
import axios from "axios";



export default {
  name: 'App',
  beforeCreate() {
    this.$store.commit("initializeStore")

    const access = this.$store.state.access
    axios.defaults.baseURL = 'http://127.0.0.1:8000';
    if ( access ) {
      axios.defaults.headers.common['Authorization'] = 'JWT ' + access
    } else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  },
    data() {
    return {
      isLoggedIn: false,
    }
  },
  mounted() {
    setInterval(() => {
      this.getAccess()
    }, 59000)
    setInterval(() => {

      this.isLoggedIn = this.getIsLoggedIn()
    }, 100)

  },
  methods: {
    getAccess() {
      const accessData = {
        refresh: this.$store.state.refresh
      }
      axios
          .post('http://127.0.0.1:8000/auth/jwt/refresh/', accessData)
          .then(response => {
            const access = response.data.access

            console.log(access)

            localStorage.setItem('access', access)
            this.$store.commit('setAccess', access)

          })
          .catch(error => {
            console.log(error)
          })
    },
    getIsLoggedIn() {
      return window.localStorage.getItem('access')
    }
  },

}

</script>

<style src="./styles/app.scss" lang="scss"/>


