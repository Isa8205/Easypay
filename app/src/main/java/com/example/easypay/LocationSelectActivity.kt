package com.example.easypay

import android.os.Bundle
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import org.json.JSONArray
import org.json.JSONObject

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

        val body = JSONObject()
        body.put("Me", "Ïsa")

        val helper = ApiHelper(applicationContext)
        val api = "http://192.168.11.67:8000/IsaTest/destinations"

        helper.get(api, object: ApiHelper.CallBack {
            override fun onSuccess(result: String?) {
                val locationJson = JSONArray(result.toString())

                (0 until locationJson.length()).forEach {
                    val location = locationJson.getJSONObject(it)

                    locations.add(
                        LocationModel(
                            location.get("name").toString(),
                            location.get("destination_id").toString(),
                            "KSH 40"
                        )
                    )
                }
            }
        })

        val adapter = LocationAdapter(locations)

        recyclerView.adapter = adapter

    }
}