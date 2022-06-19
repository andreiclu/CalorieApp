<template>
  <nav>
    <router-link to="/">Home</router-link>
    |
    <router-link to="/about">About</router-link>
    |
    <router-link to="/sign-up" v-if="!isLoggedIn">Sign up</router-link>
    |
    <router-link to="/log-in" v-if="!isLoggedIn">Log in</router-link>
    |
    <router-link to="/search">Search</router-link>
    |
    <router-link to="/meals">Meals</router-link>
    |
    <router-link to="/bmicalculator">BMI Calculator</router-link>
    |
    <router-link to="/idealbodyweight">Ideal Body Weight</router-link>
  </nav>
  <router-view/>
</template>

<script>
import axios from "axios";



export default {
  name: 'App',
  beforeCreate() {
    this.$store.commit("initializeStore")

    const access = this.$store.state.access

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
    getAccess(e) {
      const accessData = {
        refresh: this.$store.state.refresh
      }
      axios
          .post('/auth/jwt/refresh/', accessData)
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
    getIsLoggedIn(e) {
      return window.localStorage.getItem('access')
    }
  },

}

</script>


<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
