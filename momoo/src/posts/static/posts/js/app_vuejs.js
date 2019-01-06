var app2 = new Vue({
    el: '#app-2',
    data: {        
        posts: [],       
        filterDBNames: [],
        filterStatus: '',        
    },    
    mounted: function() {
        this.getPosts();
    },
    methods: {
        getPosts: function() {
            this.$http.get('/api/posts/')
                .then((response) => {
                    this.posts = response.data;
                })
                .catch((err) => {
                    console.log(err);
                })
        },
        getPostsStatusSuccess: function() {
            this.$http.get('/api/statussuccess/')
                .then((response) => {
                    this.posts = response.data;
                })
                .catch((err) => {
                    console.log(err);
                })
        },
        getPostsStatusFailed: function() {
            this.$http.get('/api/statusfailed/')
                .then((response) => {
                    this.posts = response.data;
                })
                .catch((err) => {
                    console.log(err);
                })
        },
        getBadgeStatusSuccess: function() {
            this.$http.get('/api/badgestatussuccess/')
                .then((response) => {
                    this.posts = response.data;
                })
                .catch((err) => {
                    console.log(err);
                })
        },
        getBadgeStatusFailed: function() {
            this.$http.get('/api/badgestatusfailed/')
                .then((response) => {
                    this.posts = response.data;
                })
                .catch((err) => {
                    console.log(err);
                })
        },
        getReportByStatus: function() {
            if (this.filterStatus == "Success") {
                this.getPostsStatusSuccess();
            } else {
                this.getPostsStatusFailed();
            }
        },
        getClearFilter: function() {
            this.getPosts();
        },
        getReportByDatabaseNames: function() {
            this.$http.get('/api/databasenames/')
                .then((response) => {
                    this.filterDBNames = response.data;
                })
                .catch((err) => {
                    console.log(err);
                })
        }
    }
})