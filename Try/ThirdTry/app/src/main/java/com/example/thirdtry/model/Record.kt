package com.example.thirdtry.model

import com.google.gson.annotations.SerializedName

data class Record(
    var articleName: String,
    var time: String,
    @SerializedName("article")
    var article_id: String
)