package com.example.thirdtry.ui.activity.articleDetail

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.TextView
import android.widget.Toast
import androidx.databinding.DataBindingUtil
import androidx.lifecycle.Observer
import androidx.recyclerview.widget.RecyclerView
import com.example.thirdtry.R
import com.example.thirdtry.base.BaseResponseResult
import com.example.thirdtry.databinding.ArticleCommentsLayoutBinding
import com.example.thirdtry.model.ArticleDetail
import com.example.thirdtry.model.Comment
import com.google.android.material.button.MaterialButton
import com.google.android.material.dialog.MaterialAlertDialogBuilder
import kotlinx.android.synthetic.main.activity_register.*
import kotlinx.android.synthetic.main.article_name.view.*
import android.content.DialogInterface
import android.widget.EditText
import java.text.SimpleDateFormat


class ArticleDetialBindingAdapter(
    var articleDetial: ArticleDetail, var viewModel: ArticleDetialViewModel
) : RecyclerView.Adapter<RecyclerView.ViewHolder>() {
    private val authorTYPE = 0
    private val nameTYPE = 1
    private val contentTYPE = 2
    private val timeType = 3
    private val titleTYPE = 4
    private val commentsTYPE = 5


    inner class ViewHolderComments(private val binding: ArticleCommentsLayoutBinding) :
        RecyclerView.ViewHolder(binding.root) {
        fun bind(item: Comment) {
            binding.data = item
            binding.executePendingBindings()
        }
    }

    inner class ViewHolderTitle(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val title: TextView = itemView.findViewById(R.id.title_tv) as TextView
        val add: ImageView = itemView.findViewById(R.id.add_comment)
    }

    inner class ViewHolderAuthor(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val author: TextView = itemView.findViewById(R.id.author_tv) as TextView
    }

    inner class ViewHolderName(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val name: TextView = itemView.findViewById(R.id.name_tv) as TextView
        val favButton: MaterialButton = itemView.findViewById(R.id.fav_button) as MaterialButton
    }

    inner class ViewHolderTime(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val time: TextView = itemView.findViewById(R.id.time_tv) as TextView
    }

    inner class ViewHolderContent(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val content: TextView = itemView.findViewById(R.id.content_tv) as TextView
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): RecyclerView.ViewHolder {
        val inflater = LayoutInflater.from(parent.context)
        when (viewType) {
            titleTYPE -> return ViewHolderTitle(
                inflater.inflate(
                    R.layout.article_comments_title,
                    parent,
                    false
                )
            )
            authorTYPE -> return ViewHolderAuthor(
                inflater.inflate(
                    R.layout.article_author,
                    parent,
                    false
                )
            )
            nameTYPE -> return ViewHolderName(
                inflater.inflate(
                    R.layout.article_name,
                    parent,
                    false
                )
            )
            timeType -> return ViewHolderTime(
                inflater.inflate(
                    R.layout.article_time,
                    parent,
                    false
                )
            )
            contentTYPE -> return ViewHolderContent(
                inflater.inflate(
                    R.layout.article_content,
                    parent,
                    false
                )
            )
            commentsTYPE -> {
                val binding = DataBindingUtil.inflate<ArticleCommentsLayoutBinding>(
                    inflater,
                    R.layout.article_comments_layout,
                    parent,
                    false
                )
                return ViewHolderComments(binding)
            }
            else -> return ViewHolderTitle(inflater.inflate(R.layout.scheme_title, parent, false))
        }
    }

    override fun getItemCount() = getCommentsCount() + 5
    private fun getCommentsCount() = articleDetial.comments.size

    override fun getItemViewType(position: Int): Int {
        return if (position == 0) {
            nameTYPE
        } else if (position == 1) {
            contentTYPE
        } else if (position == 2) {
            authorTYPE
        } else if (position == 3) {
            timeType
        } else if (position == 4) {
            titleTYPE
        } else {
            commentsTYPE
        }
    }

    override fun onBindViewHolder(holder: RecyclerView.ViewHolder, position: Int) {
        when (holder) {
            is ViewHolderTitle -> {
                holder.title.text = "评论"
                val inflater = LayoutInflater.from(ArticleDetialActivity.instance)
                holder.add.setOnClickListener { it1 ->
                    val view = inflater.inflate(R.layout.article_comment_edittext, null)
                    val editText = view.findViewById<EditText>(R.id.ed)
                    MaterialAlertDialogBuilder(it1.context).setView(view)
                        .setPositiveButton(R.string.text_comment,
                            DialogInterface.OnClickListener { dialog, which ->
                                if (editText.text.isEmpty()) {
                                    Toast.makeText(
                                        ArticleDetialActivity.instance,
                                        "评论不能为空",
                                        Toast.LENGTH_SHORT
                                    ).show()
                                } else {
                                    viewModel.comment(
                                        viewModel.token,
                                        articleDetial.article.id,
                                        editText.text.toString()
                                    ).observe(ArticleDetialActivity.instance,
                                        Observer {
                                            if (it == null) {
                                                Toast.makeText(
                                                    ArticleDetialActivity.instance,
                                                    "网络开小差了，请稍后",
                                                    Toast.LENGTH_SHORT
                                                ).show()
                                                return@Observer
                                            } else {
                                                if (it.success != null) {
                                                    Toast.makeText(
                                                        ArticleDetialActivity.instance,
                                                        "评论成功",
                                                        Toast.LENGTH_SHORT
                                                    ).show()
                                                    ArticleDetialActivity.instance.getData()
                                                } else {
                                                    Toast.makeText(
                                                        ArticleDetialActivity.instance,
                                                        "评论失败",
                                                        Toast.LENGTH_SHORT
                                                    ).show()
                                                }
                                            }
                                        }
                                    )
                                }

                            })
                        .setNegativeButton(R.string.text_cancel, null)
                        .show()
                }
            }
            is ViewHolderAuthor -> holder.author.text = articleDetial.article.author
            is ViewHolderContent -> holder.content.text = articleDetial.article.content
            is ViewHolderTime -> holder.time.text = articleDetial.article.time
            is ViewHolderName -> {
                holder.name.text = articleDetial.article.name
                holder.favButton.setOnClickListener {
                    viewModel.fav(viewModel.token, articleDetial.article.id)
                        .observe(ArticleDetialActivity.instance,
                            Observer {
                                if (it == null) {
                                    Toast.makeText(
                                        ArticleDetialActivity.instance,
                                        "网络开小差了，请稍后",
                                        Toast.LENGTH_SHORT
                                    ).show()
                                    return@Observer
                                } else {
                                    if (it.success != null) {
                                        Toast.makeText(
                                            ArticleDetialActivity.instance,
                                            "收藏成功",
                                            Toast.LENGTH_SHORT
                                        ).show()
                                    } else {
                                        Toast.makeText(
                                            ArticleDetialActivity.instance,
                                            "请勿重复收藏",
                                            Toast.LENGTH_SHORT
                                        ).show()
                                    }
                                }
                            })
                }
            }
            is ViewHolderComments -> holder.bind(articleDetial.comments[position - 5])
        }
    }


}