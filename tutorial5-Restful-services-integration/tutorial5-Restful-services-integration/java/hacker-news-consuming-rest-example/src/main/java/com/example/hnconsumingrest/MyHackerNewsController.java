package com.example.hnconsumingrest;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

// TODO: Class Annotations
public class MyHackerNewsController {
    private static final Logger logger = LoggerFactory.getLogger(MyHackerNewsController.class);

    // TODO: Method Annotations
    private List<HackerNewsItemRecord> hackerNewsTopStories(/* TODO: RequestParams for search */) {
        // TODO: Get IDs of top stories

        // TODO: Iterate through each ID and check if it contains the "search" terms

        return null;
    }
}
