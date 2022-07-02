<template>
  <div class="text-center">
    <v-menu
        v-model="menu"
        :close-on-content-click="false"
        :nudge-width="100"
        offset-x
    >

      <v-btn
          color="indigo"
          dark
          v-bind="attrs"
          v-on="on"
      >
        <v-tooltip top>
          <template v-slot:activator="{ on }">
            <v-btn color="primary" dark v-on="on">Top</v-btn>
          </template>
          <span>Top tooltip</span>
        </v-tooltip>
      </v-btn>


      <v-card>


        <v-list>
          <v-list-item>
            <v-text-field
                prepend-icon="mdi-scale"
                v-model="weight"
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
                    v-model="date"
                    prepend-icon="mdi-calendar"
                    readonly
                    v-bind="attrs"
                    v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                  v-model="date"
              ></v-date-picker>
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
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    let date = new Date();
    return {
      weight: 0,
      menu: false,
      date: date.toISOString().slice(0, 10),
    }
  },
  methods: {
    save() {
      axios
          .post('http://127.0.0.1:8000/api/v1/profile-info-per-day/', {date: this.date, weight: this.weight})
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