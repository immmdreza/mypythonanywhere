import dataclasses

from ...types import JsonObject


@dataclasses.dataclass(init=True, kw_only=True)
class SystemImageInfo:
    """ SystemImageInfo. """

    system_image: str
    """ The system image. """

    available_system_images: list[str]
    """ The available system images. """

    def to_json(self) -> JsonObject:
        """
        Returns:
            `dict`: The object in `dict` format.
        """

        return {
            'system_image': self.system_image,
            'available_system_images': self.available_system_images
        }
