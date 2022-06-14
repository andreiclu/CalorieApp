<template>
  <div class="sign-up-page">
    <h1> Sign Up</h1>
    <form @submit.prevent="submitForm">
      <label>Username:</label>
      <input type="email" name="username" v-model="username"> <br><br>
      <label>Password</label>
      <input type="password" name="password" v-model="password"> <br><br>
      <button type="submit">Sign Up</button>
    </form>
  </div>

</template>

<script>
import axios from "axios";

export default {
  name: "SignUp",
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    submitForm(e) {
      const formData = {
        username: this.username,
        password: this.password,
        email: this.username

      }
      axios
          .post('http://127.0.0.1:8000/auth/users/', formData)
          .then(response => {
            console.log(response)
            this.$router.push('/log-in')
          })
          .catch(error => {
            console.log(error)
          })
    }
  }
}
</script>

<style scoped>

</style>