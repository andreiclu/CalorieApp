<template>
  <v-app>
    <v-row no-gutters>
      <v-row no-gutters class="align-start">
        <v-col cols="12" class="login-part d-flex align-center justify-center flex-column">
          <div class="login-wrapper pt-md-4 pt-0">
            <v-form>
              <v-container>
                <v-row class="flex-column">
                  <v-col>
                    <p class="login-slogan display-2 text-center font-weight-medium my-10">Forgot Password!</p>

                  </v-col>
                  <v-col cols="12" class="d-flex align-center my-8">
                    <v-divider></v-divider>
                  </v-col>
                  <v-form @click="handleSubmit">
                    <v-col>
                      <v-text-field
                          v-model="email"
                          :rules="emailRules"
                          value="admin@mail.com"
                          label="Email Address"
                          required
                      ></v-text-field>

                    </v-col>
                    <v-col class="d-flex justify-center my-8">
                      <v-btn
                          class="text-capitalize"
                          large
                          :disabled="email.length === 0"
                          color="primary"

                      >
                        Submit
                      </v-btn>
                    </v-col>
                  </v-form>
                </v-row>
              </v-container>
            </v-form>
          </div>
        </v-col>
        <v-col cols="12" class="d-flex justify-center">
          <v-footer>
            <div class="primary--text">©2022 <a href="https://www.linkedin.com/in/andrei-clucerescu-449560214"
                                                class="text-decoration-none">Clucerescu Andrei</a>,
              All rights reserved.
            </div>
          </v-footer>
        </v-col>
      </v-row>
    </v-row>
  </v-app>
</template>

<script>
import axios from "axios";
export default {
  name: "Forget",
  data() {
    return {
      email: '',
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+/.test(v) || 'E-mail must be valid',
      ],
      createEmail: '',

    }
  },
  methods: {
    async handleSubmit() {
      const response = await axios.post('forget', {
        email: this.email
      });

      console.log(response);
    }
  }
}
</script>

<style src="./Froget.scss" lang="scss"/>