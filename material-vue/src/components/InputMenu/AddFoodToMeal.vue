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
                prepend-icon="mdi-pound"
                v-model="amount"
                label="Amount"
                filled
                rounded
                dense
                type="number"
            ></v-text-field>

          </v-list-item>
          <v-list-item>
            <md-autocomplete v-model="value" :md-options="countries" @md-changed="getCountries"
                             @md-opened="getCountries">
              <label>Country</label>

              <template slot="md-autocomplete-item" slot-scope="{ item }">{{ item.name }}</template>
            </md-autocomplete>
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
    mealId: Number
  },
  data() {
    return {
      menu: false,
      amount: 0,
      value: null,
      countryList: [
        {
          id: 1,
          name: 'Algeria'
        },
        {
          id: 2,
          name: 'Argentina'
        },
        {
          id: 3,
          name: 'Brazil'
        },
        {
          id: 4,
          name: 'Canada'
        },
        {
          id: 5,
          name: 'Italy'
        },
        {
          id: 6,
          name: 'Japan'
        },
        {
          id: 7,
          name: 'United Kingdom'
        },
        {
          id: 8,
          name: 'United States'
        }
      ],
      countries: []
    }
  },
  methods: {
    save() {
      axios
          .post('api/v1/foods-per-meal/', {
            number: 1,
            meal: this.mealId,
            food: 1
          })
          .then(response => {
            console.log(response)
            this.meals = response.data
          })
          .catch(error => {
            console.log(error)
          })
    },
    getCountries(searchTerm) {
      this.countries = new Promise(resolve => {
        window.setTimeout(() => {
          if (!searchTerm) {
            resolve(this.countryList)
          } else {
            const term = searchTerm.toLowerCase()

            resolve(this.countryList.filter(({name}) => name.toLowerCase().includes(term)))
          }
        }, 500)
      })
    },
  }
}
</script>