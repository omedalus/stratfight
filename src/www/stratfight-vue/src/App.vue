<template>
  <v-app>
    <v-content>
      <Combatant/>
    </v-content>
  </v-app>
</template>

<script lang="ts">
import Vue from 'vue';
import Component from 'vue-class-component';

import HelloWorld from './components/HelloWorld';
import Combatant from './components/Combatant';

// The @Component decorator indicates the class is a Vue component
@Component({
  components: {
    HelloWorld,
    Combatant
  }
})
export default class AppVue extends Vue {
  // Initial data can be declared as instance properties
  message: string = 'Hello!'

  // Component methods can be declared as instance methods
  created(): void {
    console.log('ive been created in ts');
  }
}
</script>
