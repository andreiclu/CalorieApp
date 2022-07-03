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
                prepend-icon="mdi-scale"
                v-model="goalWeight"
                label="Weight Goal"
                filled
                rounded
                dense
            ></v-text-field>

          </v-list-item>
          <v-list-item>
            <v-text-field
                prepend-icon="mdi-alpha-k-box-outline"
                v-model="goalCalories"
                label="Calorie Goal"
                filled
                rounded
                dense
            ></v-text-field>

          </v-list-item>
          <v-list-item>
            <v-text-field
                prepend-icon="mdi-human-male-height"
                v-model="height"
                label="Height"
                filled
                rounded
                dense
            ></v-text-field>


          </v-list-item>
          <v-list-item>
            <v-text-field
                prepend-icon="mdi-timer-sand"
                v-model="age"
                label="Age"
                filled
                rounded
                dense
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
    title: String,
    weightGoalDefault: Number,
    calorieGoalDefault: Number,
    heightDefault: Number,
    ageDefault: Number,
  },
  data() {
    return {
      goalWeight: this.weightGoalDefault,
      goalCalories: this.calorieGoalDefault,
      height: this.heightDefault,
      age: this.ageDefault,
      menu: false,
    }
  },
  methods: {
    save() {
      axios
          .post('http://127.0.0.1:8000/api/v1/profiles/', {
            goal_weight: this.goalWeight,
            calorie_goal: this.goalCalories,
            height: this.height,
            age: this.age
          })
          .then(response => {
            console.log(response)
            this.menu = false
            this.$emit('saved');
          })
          .catch(error => {
            console.log(error)
          })
    }
  },
  watch: {
    weightGoalDefault() {
      this.goalWeight = this.$props.weightGoalDefault
    },
    calorieGoalDefault() {
      this.goalCalories = this.$props.calorieGoalDefault
    },
    heightDefault() {
      this.height = this.$props.heightDefault
    },
    ageDefault() {
      this.age = this.$props.ageDefault
    },

  }
}
</script>