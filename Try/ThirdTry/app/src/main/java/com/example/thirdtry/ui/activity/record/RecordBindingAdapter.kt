package com.example.thirdtry.ui.activity.record

import android.content.Intent
import android.view.View
import android.widget.Toast
import com.example.thirdtry.R
import com.example.thirdtry.base.BaseBindingAdapter
import com.example.thirdtry.databinding.ArticleItemsLayoutBinding
import com.example.thirdtry.databinding.RecordItemsLayoutBinding
import com.example.thirdtry.databinding.UserCommentsBinding
import com.example.thirdtry.model.Article
import com.example.thirdtry.model.Comment
import com.example.thirdtry.model.Record
import com.example.thirdtry.ui.activity.articleDetail.ArticleDetialActivity
import org.greenrobot.eventbus.EventBus

class RecordBindingAdapter(
    items: MutableList<Record>
) : BaseBindingAdapter<Record, RecordItemsLayoutBinding>(items, R.layout.record_items_layout) {
    override fun bindItem(binding: RecordItemsLayoutBinding, item: Record) {
        binding.data = item
    }
    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.bind(items[position])
        holder.itemView.setOnClickListener(View.OnClickListener {
            val intent = Intent(it.context, ArticleDetialActivity::class.java)
            it.context.startActivity(intent)
            EventBus.getDefault().postSticky(items[position].article_id)
        })
    }
}

class CommentBindingAdapter(
    items: MutableList<Comment>
) : BaseBindingAdapter<Comment, UserCommentsBinding>(items, R.layout.user_comments) {
    override fun bindItem(binding: UserCommentsBinding, item: Comment) {
        binding.data = item
    }
    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.bind(items[position])
        holder.itemView.setOnClickListener(View.OnClickListener {
            Toast.makeText(it.context, items[position].articleName, Toast.LENGTH_SHORT).show()
//            val intent = Intent(it.context, ArticleDetialActivity::class.java)
//            it.context.startActivity(intent)
//            EventBus.getDefault().postSticky(items[position].id.toString())
        })
    }
}