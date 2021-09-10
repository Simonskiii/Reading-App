package com.example.thirdtry.ui.fragment.article
import android.content.Context
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.bumptech.glide.Glide
import com.example.thirdtry.R


class articleItemsAdapter constructor(context: Context?, d:MutableList<Map<String, Any>>?)
    : RecyclerView.Adapter<articleItemsAdapter.LinearViewHolder>() {
    private var mContext:Context? = context
    private var data: MutableList<Map<String, Any>>? = d

    inner class LinearViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val name: TextView = itemView.findViewById(R.id.article_title)
        val desc: TextView = itemView.findViewById(R.id.article_author)
    }
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): LinearViewHolder {
        return LinearViewHolder(
            LayoutInflater.from(mContext).inflate(
                R.layout.article_items_layout,
                parent,
                false
            )
        )
    }

    override fun onBindViewHolder(holder: LinearViewHolder, position: Int) {
        holder.name.text = data?.get(position)?.get("name")?.toString()
        holder.desc.text = data?.get(position)?.get("desc")?.toString()
    }

    override fun getItemCount(): Int {
        if(data?.size!! == 0){
            return 0
        }
        return data?.size!!
    }
}
