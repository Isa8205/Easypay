package com.example.easypay

import android.os.Bundle
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

class LocationSelectActivity : AppCompatActivity() {
    private lateinit var recyclerView: RecyclerView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_location_select)
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }

        recyclerView = findViewById<RecyclerView>(R.id.recycler)
        recyclerView.layoutManager = LinearLayoutManager(this)

        val locations = ArrayList<LocationModel>()

        locations.add(LocationModel("Jutmar", "CH7T7VW", "KSH 30"))
        locations.add(LocationModel("Jutmar", "CH7T7VW", "KSH 30"))
        locations.add(LocationModel("Jutmar", "CH7T7VW", "KSH 30"))
        locations.add(LocationModel("Jutmar", "CH7T7VW", "KSH 30"))
        locations.add(LocationModel("Jutmar", "CH7T7VW", "KSH 30"))

        val adapter = LocationAdapter(locations)

        recyclerView.adapter = adapter

    }
}