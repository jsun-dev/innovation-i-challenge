<template>
  <v-col align="center">
    <h1>Home Page</h1>
    <p class="mt-1">
      A simple application with two tables: the 
      Employee table and a newly-created Task table.<br />
      Feel free to view them using the navigation bar or the buttons below.
    </p>
    <v-row justify="center" class="mt-4">
      <v-btn to="/employee" variant="text" style="width: 150px" nuxt>Employees</v-btn>
      <v-btn to="/task" variant="text" class="ml-8" style="width: 150px" nuxt>Tasks</v-btn>
    </v-row>
  </v-col>
</template>

<script>
export default {}
</script>

<style></style>
