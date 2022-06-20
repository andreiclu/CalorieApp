<template>
  <v-app>
    <v-container fluid>
      <v-row no-gutters>
        <v-col cols="7" class="main-part d-none d-md-none d-lg-flex">
          <div class="d-flex">
            <v-img src="@/assets/logo.svg" contain></v-img>
            <p>Calorie Calculator</p>
          </div>
        </v-col>
        <v-col cols="12" lg="5" class="login-part d-flex align-center justify-center">
          <v-row no-gutters class="align-start">
            <v-col cols="12" class="login-part d-flex align-center justify-center flex-column">
              <div class="login-wrapper pt-md-4 pt-0">
                <v-tabs grow>
                  <v-tabs-slider></v-tabs-slider>
                  <v-tab :href="`#tab-login`">
                    LOGIN
                  </v-tab>
                  <v-tab :href="`#tab-newUser`">
                    New User
                  </v-tab>

                  <v-tab-item :value="'tab-login'">
                    <v-form>
                      <v-container>
                        <v-row class="flex-column">
                          <v-col>
                            <p class="login-slogan display-2 text-center font-weight-medium my-10">Good Morning,
                              User</p>

                          </v-col>
                          <v-col cols="12" class="d-flex align-center my-8">
                            <v-divider></v-divider>
                          </v-col>
                          <v-form>
                            <v-col>
                              <v-text-field
                                  v-model="email"
                                  :rules="emailRules"
                                  value="admin@mail.com"
                                  label="Email Address"
                                  required
                              ></v-text-field>
                              <v-text-field
                                  v-model="password"
                                  :rules="passRules"
                                  type="password"
                                  label="Password"
                                  hint="At least 8 characters"
                                  required
                              ></v-text-field>

                            </v-col>
                            <v-col class="d-flex justify-space-between">
                              <v-btn
                                  class="text-capitalize"
                                  large
                                  :disabled="password.length === 0 || email.length === 0"
                                  color="primary"
                                  @click="login"
                              >
                                Login
                              </v-btn>
                              <v-btn large text class="text-capitalize primary--text">Forget Password</v-btn>
                            </v-col>
                          </v-form>
                        </v-row>
                      </v-container>
                    </v-form>
                  </v-tab-item>

                  <v-tab-item :value="'tab-newUser'">
                    <v-form>
                      <v-container>
                        <v-row class="flex-column">

                          <v-col>
                            <p class="login-slogan display-2 text-center font-weight-medium mt-10">Welcome!</p>
                            <p class="login-slogan display-1 text-center font-weight-medium mb-10">Create your
                              account</p>
                          </v-col>

                          <v-form>
                            <v-col>
                              <v-text-field
                                  v-model="createEmail"
                                  :rules="emailRules"
                                  label="Email Address"
                                  required
                              ></v-text-field>
                              <v-text-field
                                  v-model="createPassword"
                                  :rules="passRules"
                                  type="password"
                                  label="Password"
                                  hint="At least 8 characters"
                                  required
                              ></v-text-field>
                            </v-col>
                            <v-col class="d-flex justify-space-between">
                              <v-btn
                                  large
                                  block
                                  :disabled="createEmail.length === 0 || createPassword === 0"
                                  color="primary"
                                  @click="signup"
                              >
                                Create your account
                              </v-btn>
                            </v-col>
                          </v-form>
                        </v-row>
                      </v-container>
                    </v-form>
                  </v-tab-item>

                </v-tabs>
              </div>
            </v-col>
            <v-col cols="12" class="d-flex justify-center">
              <v-footer>
                <div class="primary--text">©2022 <a href="https://www.linkedin.com/in/andrei-clucerescu-449560214" class="text-decoration-none">Clucerescu Andrei</a>,
                  All rights reserved.
                </div>
              </v-footer>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>

import axios from "axios";

export default {
  name: 'Login',
  data() {
    return {
      email: '',
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+/.test(v) || 'E-mail must be valid',
      ],
      createEmail: '',
      createPassword: '',
      password: '',
      passRules: [
        v => !!v || 'Password is required',
        v => v.length >= 8 || 'Min 8 characters',
        v => /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/.test(v) || 'Password is insecure',
      ]
    }
  },
  methods: {
    signup() {
      const formData = {
        username: this.createEmail,
        password: this.createPassword,
        email: this.createEmail

      }
      console.log(formData)


      axios
          .post('http://127.0.0.1:8000/auth/users/', formData)
          .then(response => {
            console.log(response)
            this.username = this.createEmail
            this.password = this.createPassword
            this.login()
          })
          .catch(error => {
            console.log(error)
          })
    },

    login() {
      axios.defaults.headers.common['Authorization'] = ''
      localStorage.removeItem('access')

      const formData = {
        username: this.username,
        password: this.password
      }
      axios
          .post('http://127.0.0.1:8000/auth/jwt/create/', formData)
          .then(response => {
            console.log(response)

            const access = response.data.access
            const refresh = response.data.refresh

            this.$store.commit('setAccess', access)
            this.$store.commit('setRefresh', refresh)

            axios.defaults.headers.common['Authorization'] = 'JWT ' + access

            localStorage.setItem('access', access)
            localStorage.setItem('refresh', refresh)
            window.localStorage.setItem('authenticated', true);
            this.$router.push('/dashboard');
            this.$router.push('/')

          })
          .catch(error => {
            console.log(error)
          })
    }
  },
  created() {
    if (window.localStorage.getItem('authenticated') === 'true') {
      this.$router.push('/dashboard');
    }
  },



}

</script>

<style src="./Login.scss" lang="scss"/>
