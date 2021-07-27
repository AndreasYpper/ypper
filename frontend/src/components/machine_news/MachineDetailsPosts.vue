<template>
  <div class="posts-container">
    <div class="header">
      <h1>Machine Posts</h1>
    </div>
    <div class="button-group">
      <div class="show-form" v-if="!getShowCreatePost()">
        <button class="create-button" @click="toggleCreateForm()">
          Create New Posts
        </button>
      </div>
    </div>
    <div class="create-form" v-if="getShowCreatePost()">
      <CreateMachinePost />
    </div>
    <div class="active-posts">
      <p>Here is all active posts</p>
    </div>
  </div>
</template>

<script>
import CreateMachinePost from "@/components/machine_news/CreateMachinePost";
import stateMachine from '@/modules/machine'
export default {
  props: {
    machine: {
      required: true,
      type: Object,
    },
  },
  components: {
    CreateMachinePost,
  },
  setup() {
    const { getShowCreatePost, toggleShowCreatePost } = stateMachine

    function toggleCreateForm() {
      toggleShowCreatePost()

    }

    return {
      getShowCreatePost,
      toggleCreateForm,
    };
  },
};
</script>

<style scoped>
</style>