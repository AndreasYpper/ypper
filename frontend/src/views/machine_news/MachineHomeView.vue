<template>
  <div class="machine-news-container">
    <div class="header">
          <h1>Machine News</h1>
    </div>
    <button @click="open_modal">Create machine</button>
    <div class="create-machine-modal" v-if="create_modal">
      <CreateMachine />
    </div>
  </div>
</template>

<script>
import CreateMachine from '@/components/machine_news/CreateMachine'
import { ref } from 'vue'
export default {
  components: {
    CreateMachine
  },
  setup() {
    const create_modal = ref(false)

    function open_modal() {
      create_modal.value = true
    }

    return {
      create_modal,
      open_modal
    }
  }
}
</script>

<style scoped>
.machine-news-container{
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto;
}
.header{
  grid-column: 1 / 4;
  grid-row: 1;
}
.create-machine-modal {
  position: fixed; /* Stay in place */
  z-index: 1; /* Sit on top */
  padding-top: 100px; /* Location of the box */
  left: 0;
  top: 0;
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  overflow: auto; /* Enable scroll if needed */
  background-color: rgb(0,0,0); /* Fallback color */
  background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
}
.modal-backdrop {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background-color: rgba(0, 0, 0, 0.3);
  z-index: 1;
}
</style>