<template>
  <v-footer class="px-0 mt-10" color="transparent">
    <v-row no-gutters>
      <div>
        <v-btn
              v-for="link in links"
              :key="link.link"
              color="primary"
              text
              :href="link.link"
              class="text-capitalize ml-1 font-weight-regular"
          >
            {{ link.text }}
          </v-btn>
      </div>
      <div>
        <v-btn
                v-for="icon in icons"
                :key="icon.icon"
                :href="icon.link"
                class="mr-1"
                :color=config.light.textColor
                icon
        >
          <v-icon size="24px">{{ icon.icon }}</v-icon>
        </v-btn>
      </div>
    </v-row>
  </v-footer>
</template>

<script>
import config from '../../config';

export default {
  name: 'Footer',

  data: () => ({
    config,
    icons: [
      {icon: 'mdi-facebook', link: 'https://www.facebook.com/andrei.clu/'},
      {icon: 'mdi-linkedin', link: 'https://www.linkedin.com/in/andrei-clucerescu-449560214'},
      {icon: 'mdi-github', link: 'https://github.com/andreiclu/'},

    ],
    links: [
      {text: 'Other Calculators', link: 'https://www.calculator.net/fitness-and-health-calculator.html'},
      {text: 'Blog', link: 'https://www.obio.ro/blog/alimentatie-sanatoasa/'},
    ]
  }),
}
</script>

<style src="./Footer.scss" lang="scss"/>

