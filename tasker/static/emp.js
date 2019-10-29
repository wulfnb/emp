// var csrftoken = Cookies.get('csrftoken');
// Vue.http.headers.common['HTTP_X_CSRFTOKEN'] = csrftoken;
const app = new Vue({
    el: '#employee',

    delimiters: ["<%", "%>"],


    data: {
        name : 'Test',
        task_list: null,
        csrf_token1: '',
        get_query : `query{
            allUser: employee(id:1){
              id
              username
              taskSet{
                id
                task
                status
              }
            }
          }`
    },

    computed: {
        
    },
    mounted() {
        // this.csrf_token = Cookies.get('csrftoken');
    },
    methods: {

        getAllTasks() {
            // csrftoken = Cookies.get('csrftoken');

            fetch('/emp/graphql', {
                method: 'POST',
                credentials: 'include',
                headers: {
                    "Content-Type": "application/json"
                },
                // headers : {X_CSRFTOKEN: csrftoken},
                body: JSON.stringify({ query: this.get_query }),
            }).then(response => {
                return response.json()
            }).then(json => {
                this.task_list = json.data.allUser.taskSet
            })
        
        },
    }
})