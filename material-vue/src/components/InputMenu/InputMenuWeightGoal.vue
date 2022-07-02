<template>
  <v-layout justify-center>
    <v-menu top
        v-model="menu"
        :close-on-content-click="false"
        :nudge-width="100"
            offset-x

    >
      <template v-slot:activator="{ on, attrs }">

          <v-btn
              color="indigo"
              dark
              v-bind="attrs"
              v-on="on"

          >
            {{ title }}
          </v-btn>
      </template>
      <v-card>


        <v-list>
          <v-list-item>
            <v-text-field
                prepend-icon="mdi-scale"
                v-model="weightGoal"
            ></v-text-field>

          </v-list-item>
        </v-list>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn
              text
              @click="menu = false"
          >
            Cancel
          </v-btn>
          <v-btn
              color="primary"
              text
              @click="save"
          >
            Save
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-menu>
  </v-layout>
</template>

<script>
import axios from "axios";

export default {
  props: {
    title: String
  },
  data() {
    return {
      weightGoal: 0,
      menu: false,
    }
  },
  methods: {
    save() {
      axios
          .post('http://127.0.0.1:8000/api/v1/profiles/', {goal_weight: this.weightGoal})
          .then(response => {
            console.log(response)
            this.menu = false
            this.$emit('saved');
          })
          .catch(error => {
            console.log(error)
          })
    }
  }
}
</script>