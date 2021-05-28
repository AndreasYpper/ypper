<template>
  <div class="navbar-container">
    <div class="nav-item home">
      <router-link :to="{ name: 'machine_news_home' }" class="link"
        >Home</router-link
      >
    </div>
    <div class="nav-item create-machine">
      <button class="link" @click="openCreateModal()">Create Machine</button>
    </div>

    <!-- Create machine modal -->
    <transition name="create-machine" appear>
    <div class="create-machine-modal" v-if="create_modal">
      <div class="modal-backdrop" @click="closeCreateModal()" />
      <div class="modal-dialog">
        <div class="modal-header">
          <span class="modal-close" @click="closeCreateModal()"> &times; </span>
        </div>
        <div class="modal-body">
          <CreateMachine />
        </div>
      </div>
    </div>
    </transition>
  </div>
</template>

<script>
import CreateMachine from '@/components/machine_news/CreateMachine'
import { ref, onMounted } from 'vue'
import stateSite from '@/modules/site'
export default {
  components: {
    CreateMachine
  },
  setup() {
    const create_modal = ref(false)
    const { setSite } = stateSite

    onMounted(() => {
      setSite('machine_news')
    })

    function openCreateModal() {
      create_modal.value = true
    }

    function closeCreateModal() {
      create_modal.value = false
    }

    return {
      create_modal,
      openCreateModal,
      closeCreateModal
    }
  }
}
</script>

<style scoped>
.navbar-container {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto;
  justify-items: center;
  align-items: center;
}
.nav-item {
  padding: 10px;
  cursor: pointer;
  border-radius: 15px;
}
/* .nav-item:hover {
  background-color: #f8cacb;
} */
.link {
  padding: 10px;
  text-decoration: none;
  color: #ff3b3f;
  font-weight: bold;
  font-family: "Ubuntu", sans-serif;
  border: none;
  font-size: 1vw;
  border-radius: 15px;
  padding: 10px;
  cursor: pointer;
}
.link:hover {
  background-color: #f8cacb;
}
.home {
  grid-column: 2 / 4;
}
.create-machine {
  grid-column: 5 / 7;
}
.create-machine-enter-from {
  opacity: 0;
}
.create-machine-enter-to {
  opacity: 1;
}
.create-machine-enter-active {
  transition: all 0.5s ease;
}
.create-machine-leave-from {
  opacity: 1;
}
.create-machine-leave-to {
  opacity: 0;
}
.create-machine-leave-active {
  transition: all 0.25s ease;
}
.create-machine-modal {
  position: fixed; /* Stay in place */
  top: 0;
  right: 0;
  left: 0;
  z-index: 9;
  overflow-x: hidden;
  overflow-y: auto;
  display: grid;
  grid-template-rows: auto;
  grid-template-columns: repeat(12, 1fr);
}
.modal-backdrop {
  position: fixed;
  width: 100%;
  height: 100%;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background-color: rgba(0, 0, 0, 0.3);
  z-index: 1;
}
.modal-dialog {
  position: relative;
  z-index: 2;
  grid-column: 5 / 9;
  grid-row: 1;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto;
  margin-top: 100px;
  background-color: #fefefe;
  border-radius: 10px;
}
.modal-header {
  grid-column: 1 / 13;
  grid-row: 1;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto;
}
.modal-close {
    cursor: pointer;
    margin: 0 3px 0 10px;
    font-size: 1.5vw;
    grid-column: 12;
}
.modal-body {
  grid-column: 1 / 13;
  grid-row: 2;
}
</style>