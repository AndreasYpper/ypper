<template>
  <div class="profile-container">
      <div class="profile" v-if="user.authenticated">
          <h1>You are signed in!</h1>
      </div>
      <div class="authentication" v-if="!user.authenticated">
        <Authentication />
      </div>
  </div>
</template>

<script>
import Authentication from '@/components/authentication/Authentication'
import stateUser from '@/modules/user'
export default {
  components: {
    Authentication
  },
  setup() {
    const { getUser } = stateUser
    const user = getUser()

    return {
      getUser,
      user
    }
  }
}
</script>

<style>

</style>