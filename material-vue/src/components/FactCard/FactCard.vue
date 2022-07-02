<template>
  <v-card class="mx-1 mb-1" :color="type" :dark="!!type"
  >

    <v-card-text class=text-center>
      <v-layout row wrap text-xs-center>

        <v-flex xs12>
          <slot><h3 style="padding: 13px">{{ title }}</h3></slot>
        </v-flex>


        <v-flex xs12>
          <h1>{{ value }} {{ unit }}</h1>
        </v-flex>
        <v-flex xs12>
          {{ description }}
        </v-flex>
      </v-layout>

    </v-card-text>
  </v-card>
</template>

<script>
export default {

  name: 'FactCard',
  props: {
    type: String,
    title: String,
    value: Number,
    unit: String,
    description: String

  }

}
</script>
