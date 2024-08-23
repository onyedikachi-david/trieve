/**
 * This includes all the functions you can use to communicate with our Events API
 *
 * @module Event Methods
 */

import { GetEventsData } from "../../fetch-client";
import { TrieveSDK } from "../../sdk";

export async function getEventsForDataset(
  /** @hidden */
  this: TrieveSDK,
  data: GetEventsData,
  signal?: AbortSignal
) {
  return await this.trieve.fetch(
    "/api/events",
    "post",
    {
      data,
      datasetId: this.datasetId,
    },
    signal
  );
}