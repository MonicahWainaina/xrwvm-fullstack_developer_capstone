import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import "./Dealers.css";
import "../assets/style.css";
import positive_icon from "../assets/positive.png"
import neutral_icon from "../assets/neutral.png"
import negative_icon from "../assets/negative.png"
import review_icon from "../assets/reviewbutton.png"
import Header from '../Header/Header';

const Dealer = () => {
  const [dealer, setDealer] = useState(null); // Initialize dealer as null
  const [reviews, setReviews] = useState([]);
  const [unreviewed, setUnreviewed] = useState(false);
  const [postReview, setPostReview] = useState(<></>);
  const [loadingDealer, setLoadingDealer] = useState(true); // Add loading state
  const [dealerError, setDealerError] = useState(null); // Add error state

  let curr_url = window.location.href;
  let root_url = curr_url.substring(0, curr_url.indexOf("dealer"));
  let params = useParams();
  let id = params.id;
  let dealer_url = root_url + `djangoapp/dealer/${id}`;
  let reviews_url = root_url + `djangoapp/reviews/dealer/${id}`;
  let post_review = root_url + `postreview/${id}`;

  const get_dealer = async () => {
    setLoadingDealer(true);
    setDealerError(null);
    try {
      const res = await fetch(dealer_url, {
        method: "GET"
      });
      const retobj = await res.json();

      if (retobj.status === 200 && retobj.dealer) { // Changed this line
        setDealer(retobj.dealer); // Changed this line
      } else {
        setDealerError("Failed to load dealer details.");
        console.error("Error fetching dealer details:", retobj);
      }
    } catch (error) {
      setDealerError("Network error loading dealer details.");
      console.error("Network error fetching dealer details:", error);
    } finally {
      setLoadingDealer(false);
    }
  };

  const get_reviews = async () => {
    const res = await fetch(reviews_url, {
      method: "GET"
    });
    const retobj = await res.json();

    if (retobj.status === 200) {
      if (retobj.reviews && retobj.reviews.length > 0) {
        setReviews(retobj.reviews);
      } else {
        setUnreviewed(true);
      }
    } else {
      console.error("Error fetching reviews:", retobj);
      // Optionally set an error state for reviews
    }
  };

  const senti_icon = (sentiment) => {
    let icon = sentiment === "positive" ? positive_icon : sentiment === "negative" ? negative_icon : neutral_icon;
    return icon;
  };

  useEffect(() => {
    get_dealer();
    get_reviews();
    if (sessionStorage.getItem("username")) {
      setPostReview(<a href={post_review}><img src={review_icon} style={{ width: '10%', marginLeft: '10px', marginTop: '10px' }} alt='Post Review' /></a>)
    }
  }, [id, post_review]); // Add id and post_review to dependency array

  return (
    <div style={{ margin: "20px" }}>
      <Header />
      <div style={{ marginTop: "10px" }}>
        {loadingDealer ? (
          <h1 style={{ color: "grey" }}>Loading Dealer Details...</h1>
        ) : dealerError ? (
          <h1 style={{ color: "red" }}>{dealerError}</h1>
        ) : dealer ? (
          <h1 style={{ color: "grey" }}>{dealer.full_name}{postReview}</h1>
        ) : (
          <h1 style={{ color: "grey" }}>Dealer Details Not Found</h1>
        )}
        {dealer && (
          <h4 style={{ color: "grey" }}>
            {dealer.city},{dealer.address}, Zip - {dealer.zip}, {dealer.state}
          </h4>
        )}
      </div>
      <div className="reviews_panel">
        {reviews.length === 0 && unreviewed === false ? (
          <text>Loading Reviews....</text>
        ) : unreviewed === true ? (
          <div>No reviews yet!</div>
        ) : (
          reviews.map(review => (
            <div className='review_panel' key={review._id || Math.random()}> {/* Added a key for mapping */}
              <img src={senti_icon(review.sentiment)} className="emotion_icon" alt='Sentiment' />
              <div className='review'>{review.review}</div>
              <div className="reviewer">{review.name} {review.car_make} {review.car_model} {review.car_year}</div>
            </div>
          ))
        )}
      </div>
    </div>
  );
}

export default Dealer;