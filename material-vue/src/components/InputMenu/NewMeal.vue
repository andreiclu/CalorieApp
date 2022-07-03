<template>
  <v-layout justify-end>
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
                prepend-icon="mdi-text"
                v-model="newMealTitle"
                label="Name"
                filled
                rounded
                dense
            ></v-text-field>

          </v-list-item>
          <v-list-item>
            <v-menu
                :close-on-content-click="false"
                transition="scale-transition"
                offset-y
                min-width="auto"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                    v-model="newMealDate"
                    prepend-icon="mdi-calendar"
                    readonly
                    v-bind="attrs"
                    v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                  v-model="newMealDate"
              ></v-date-picker>
            </v-menu>

          </v-list-item>
          <v-list-item>
            <v-menu
                :close-on-content-click="false"
                transition="scale-transition"
                offset-y
                min-width="auto"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                    v-model="newMealTime"
                    prepend-icon="mdi-clock"
                    readonly
                    v-bind="attrs"
                    v-on="on"
                ></v-text-field>
              </template>
              <v-time-picker
                  v-model="newMealTime"
              ></v-time-picker>
            </v-menu>

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
    title: String,
    weightGoalDefault: Number,
    calorieGoalDefault: Number,
    heightDefault: Number,
    ageDefault: Number,
  },
  data() {
    let date = new Date()
    return {
      menu: false,
      newMealTime: date.toTimeString().split(' ')[0].slice(0, -3),
      newMealTitle: "",
      newMealDate: date.toISOString().slice(0, 10),
    }
  },
  methods: {
    save() {
      axios
          .post('api/v1/meals/', {
            date: this.newMealDate,
            time: this.newMealTime,
            title: this.newMealTitle
          })
          .then(response => {
            console.log(response)
            this.meals = response.data
          })
          .catch(error => {
            console.log(error)
          })
    }
  },
}
</script>