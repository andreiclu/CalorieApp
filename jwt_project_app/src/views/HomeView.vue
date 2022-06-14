<template>
  <div v-if='isLoggedIn' class="home">
       <div class="header">
      <h1>Home</h1>
      <h3> Welcome {{user_data}}</h3>
      <input v-if="isLoggedIn" type="button" value="Logout" v-on:click="logout"/>
    </div>
    <table>
    <tr>
      <td>Username</td>
      <td>Weight</td>
      <td>Height</td>
      <td>Age</td>
      <td>Gender</td>
      <td>Lifestyle</td>
    </tr>
    <tr>
      <td :src="user_data">{{user_data}}</td>
      <td :src="profile_weight">{{profile_weight}}</td>
      <td :src="profile_height">{{profile_height}}</td>
      <td :src="profile_age">{{profile_age}}</td>
      <td :src="profile_gender">{{profile_gender}}</td>
    </tr>
  </table>

  </div>


</template>

<script>

import axios from "axios"

export default {
  name: 'HomeView',
  data() {
    return {
      user_data: '',
      profile_weight: '',
      profile_height: '',
      profile_age: '',
      profile_gender: '',
      food: ''
    }
  },
  mounted() {
    this.getMe()
    this.getProfileDetails()
    this.getFood()
  },
  methods: {
    getMe(e) {
      axios
          .get('auth/users/me/')
          .then(response => {
            console.log(response)
            this.user_data = response.data.username
          })
          .catch(error => {
            console.log(error)
          })
    },
    getProfileDetails(e) {
      axios
          .get('/api/v1/profiles/')
          .then(response => {
            console.log(response)
            this.profile_weight = response.data.weight
            this.profile_height = response.data.height
            this.profile_age = response.data.age
            this.profile_gender = response.data.gender


          })
          .catch(error => {
            console.log(error)
          })


    },
    logout() {
      localStorage.clear()
      this.$router.push('/log-in')
    },
    getFood(e) {

    }

  },
  computed: {
    isLoggedIn() {
      return !!window.localStorage.getItem('access')
    }
  }
}
</script>