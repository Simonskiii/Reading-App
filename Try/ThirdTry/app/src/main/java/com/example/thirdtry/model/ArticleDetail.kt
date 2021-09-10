package com.example.thirdtry.model

data class ArticleDetail(
    var article: Article1,
    var comments: MutableList<Comment>
)

data class Article1(
    var author: String,
    var comment_num: Int,
    var content: String,
    var fav_num: Int,
    var id: Int,
    var name: String,
    var time: String
)

data class Comment(
    var article: Int,
    var content: String,
    var time: String,
    var userName : String,
    var articleName : String
)