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
            <v-card>
              <v-card-text>
                <v-autocomplete
                    v-model="food"
                    :items="items"
                    :loading="isLoading"
                    :search-input.sync="search"
                    color="white"
                    hide-no-data
                    hide-selected
                    item-text="name"
                    item-value="API"
                    label="Search"
                    placeholder="Start typing to Search"
                    prepend-icon="mdi-database-search"
                    return-object
                ></v-autocomplete>
              </v-card-text>
              <v-divider></v-divider>
              <v-expand-transition>
                <v-list
                    v-if="food"
                    class="lighten-3"
                >
                  <v-list-item
                      v-for="(field, i) in fields"
                      :key="i"
                  >
                    <v-list-item-content>
                      <v-list-item-title v-text="field.value"></v-list-item-title>
                      <v-list-item-subtitle v-text="field.key"></v-list-item-subtitle>
                    </v-list-item-content>
                  </v-list-item>
                </v-list>
              </v-expand-transition>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                    :disabled="!food"
                    color="primary"
                    @click="food = null"
                >
                  Clear
                  <v-icon right>
                    mdi-close-circle
                  </v-icon>
                </v-btn>
              </v-card-actions>
            </v-card>
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
      descriptionLimit: 60,
      entries: [],
      isLoading: false,
      food: null,
      search: null,
    }
  },
  methods: {
    save() {
      console.log(this.food)
      axios
          .post('api/v1/foods-per-meal/', {
            number: this.amount,
            meal: this.mealId,
            food: this.food.id
          })
          .then(response => {
            console.log(response)
            this.menu = false
            this.$emit('saved')
          })
          .catch(error => {
            console.log(error)
          })
    }
  },
  computed: {
    fields() {
      if (!this.food) return []

      return Object.keys(this.food).filter(key => {
        return !["id", "category", "name", "serving_size", "calories", "carbohydrate", "protein", "total_fats"].includes(key);

      }).map(key => {

        return {
          key,
          value: this.food[key] || 'n/a',
        }
      })
    },
    items() {
      return this.entries.map(entry => {
        return Object.assign({}, entry, {
          Name: entry.name, "Serving Size": entry.serving_size,
          Calories: entry.calories, Carbs: entry.carbohydrate, Proteins: entry.protein, Fats: entry.total_fats
        })
      })
    },
  },
  watch: {
    search(val) {
      if (this.isLoading) return

      this.isLoading = true

      // Lazily load input items
      axios
          .get('api/v1/foods/', {params: {search: val}})
          .then(response => {
            this.count = response.data.results.length
            this.entries = response.data.results
          })
          .catch(err => {
            console.log(err)
          })
          .finally(() => (this.isLoading = false))
    },
  },
}
</script>