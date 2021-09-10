package com.example.thirdtry.base

import com.google.gson.annotations.SerializedName

data class BaseResult(
    @SerializedName("code")
    var code: Int?,
    @SerializedName("msg")
    var message: String?,
    @SerializedName("success")
    var success: String?,
    @SerializedName("error")
    var error: String?
)